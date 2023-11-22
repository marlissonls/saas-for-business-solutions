import { useState } from 'react'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Dashboard from "./pages/dashboard";
import DashboardCards from "./pages/dashboardCards";
import LandingPage from "./pages/landingPage.jsx";
import Login from "./pages/login";
import MlModel from "./pages/mlModel";
import MlModelCards from "./pages/mlModelCards";
import Welcome from "./pages/welcome";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/dashboardcards",
    element: <DashboardCards />,
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
  },
  {
    path: "/mlmodelcards",
    element: <MlModelCards />,
  },
  {
    path: "/mlmodel",
    element: <MlModel />,
  },
  {
    path: "/welcome",
    element: <Welcome />,
  },

]);
import './App.css'

function App() {
  return <div>
    <RouterProvider router={router} />
  </div>
}

export default App
