import axios from "axios"
import { get_token, logout } from "./auth"
import { redirect } from 'react-router-dom';

const HOST_API = "http://localhost"

const api = axios.create({
    baseURL: HOST_API,
  });

api.interceptors.request.use(
  (config) => {
    config.headers.Authorization = `Bearer ${get_token()}`;
    return config;
  },
  (error) => Promise.reject(error),
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const {
      response: { status },
    } = error;

    if (status === 403) {
      logout()
      redirect('/login')
    }
    return Promise.reject(error);
  },
);

export default api