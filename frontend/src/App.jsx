import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Dashboard from "./pages/dashboard";
import DashboardCards from "./pages/dashboardCards";
import LandingPage from "./pages/landingPage";
import Login from "./pages/login";
import MlModel from "./pages/mlModel";
import MlModelCards from "./pages/mlModelCards";
import Welcome from "./pages/welcome";
import { SnackbarProvider } from 'notistack';

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
    <SnackbarProvider>
      <RouterProvider router={router} />
    </SnackbarProvider>
  </div>
}

export default App
