import React from "react";
import { useParams } from "react-router-dom";

function Dashboard(props) {
    const { id } = useParams();
    return <div>Dashboard</div>
}

export default Dashboard