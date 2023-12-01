import { createBrowserRouter, RouterProvider, redirect } from "react-router-dom";
import Dashboard from "./pages/dashboard";
import DashboardCards from "./pages/dashboardCards";
import LandingPage from "./pages/landingPage";
import Login from "./pages/login";
import MlModel from "./pages/mlModel";
import MlModelCards from "./pages/mlModelCards";
import Welcome from "./pages/welcome";
import { SnackbarProvider } from 'notistack';
import { isAuthenticated } from "./services/auth";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
    loader: async () => {
      if (isAuthenticated()) throw new redirect("/welcome");
      return {}
    }
  },
  {
    path: "/login",
    element: <Login />,
    loader: async () => {
      if (isAuthenticated()) throw new redirect("/welcome");
      return {}
    }
  },
  {
    path: "/dashboardcards",
    element: <DashboardCards />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/login");
      return {}
    }
  },
  {
    path: "/dashboard/:id",
    element: <Dashboard />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/login");
      return {}
    }
  },
  {
    path: "/mlmodelcards",
    element: <MlModelCards />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/login");
      return {}
    }
  },
  {
    path: "/mlmodel",
    element: <MlModel />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/login");
      return {}
    }
  },
  {
    path: "/welcome",
    element: <Welcome />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/login");
      return {}
    }
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
