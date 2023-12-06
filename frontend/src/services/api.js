import axios from "axios"
import { get_token } from "./auth"

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

// api.interceptors.response.use(
//   (response) => response,
//   (error) => {
//     const {
//       config,
//       response: { status },
//     } = error;
//     const originalRequest = config;

//     if (status === 401) {
//       const retryOrigReq = new Promise((resolve) => {
//         resolve(
//           axios({
//             method: 'GET',
//             url: `${HOST_API}/newToken`,
//             headers: { refreshToken: getRefreshToken() },
//           }),
//         );
//       }).then((result) => {
//         if (result.data.status) {
//           setNewToken(result.data.token);
//           return new Promise((resolve) => {
//             originalRequest.headers.Authorization = `Bearer ${result.data.token}`;
//             resolve(axios(originalRequest));
//           });
//         }
//         return Promise.reject(error);
//       });
//       return retryOrigReq;
//     }
//     return Promise.reject(error);
//   },
// );

export default api