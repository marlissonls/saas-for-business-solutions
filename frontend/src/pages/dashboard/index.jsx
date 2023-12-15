import React, { useState, useEffect }from "react";
import { useParams } from "react-router-dom";

import api from "../../services/api";
import SideBar from "../../components/sideBar";
import MainContent from "../../containers/mainContent";

import Dash1 from "./dashInterfaces/dash1";
import Dash2 from "./dashInterfaces/dash2";

function selectDash(id, data) {
    switch (id) {
        case 'a23e4567-e89b-12d3-a456-426614174001': return <Dash1 data={ data }/>
        case '2': return <Dash2 data={ data }/>
        default: return null
    }
}

async function getDashboard(id) {
    // const response = await api.get(`/dashboards/${id}`)
    // return response.data
    return 'teste'
}

function Dashboard(props) {
    const { id } = useParams();
    const [data, setData] = useState(null)
    useEffect(() => {
        async function updateData() {
            const data = await getDashboard(id)
            setData(data)
        }
        updateData()
    }, [id])
    return <div className='body'>
        <SideBar />
        <MainContent>
            { data ? selectDash(id, data) : <div>Buscando os dados...</div> }
        </MainContent>
    </div>
}

export default Dashboard;