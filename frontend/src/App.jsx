import { createBrowserRouter, RouterProvider, redirect } from "react-router-dom";
import LandingPage from "./pages/landingPage";
import Home from "./pages/home";
import DashboardCards from "./pages/dashboardCards";
import Dashboard from "./pages/dashboard";
import MlModelCards from "./pages/mlModelCards";
import MlModel from "./pages/mlModel";
import Panel from "./pages/panel";
import { SnackbarProvider } from 'notistack';
import { isAdmin, isAuthenticated } from "./services/auth";
import './App.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
    loader: async () => {
      if (isAuthenticated() && !isAdmin()) throw new redirect("/home");
      if (isAuthenticated() && isAdmin()) throw new redirect("/panel");
      return {}
    }
  },
  {
    path: "/home",
    element: <Home />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/");
      if (isAdmin()) throw new redirect("/panel");
      return {}
    }
  },
  {
    path: "/dashboards",
    element: <DashboardCards />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/");
      return {}
    }
  },
  {
    path: "/dashboards/:id",
    element: <Dashboard />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/");
      return {}
    }
  },
  {
    path: "/models",
    element: <MlModelCards />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/");
      return {}
    }
  },
  {
    path: "/models/:id",
    element: <MlModel />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/");
      return {}
    }
  },
  {
    path: "/panel",
    element: <Panel />,
    loader: async () => {
      if (!isAuthenticated()) throw new redirect("/");
      if (!isAdmin()) throw new redirect("/home");
      return {}
    }
  },
]);

function App() {
  return <div>
    <SnackbarProvider>
      <RouterProvider router={router} />
    </SnackbarProvider>
  </div>
}

export default App;