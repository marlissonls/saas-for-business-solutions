import React, { useState, useEffect }from "react";
import { useParams } from "react-router-dom";

import api from "../../services/api";
import SideBar from "../../components/sideBar";
import MainContent from "../../components/mainContent";

import Model1 from "./modelInterfaces/model1";
import Model2 from "./modelInterfaces/model2";

function selectModel(id, data) {
    switch (id) {
        case 1: return <Model1 data={ data }/>
        case 2: return <Model2 data={ data }/>
        default: return null
    }
}

async function getModel(id) {
    const response = await api.get(`/models/${id}`)
    return response.data
}

function Model(props) {
    const { id } = useParams();
    const [data, setData] = useState(null)
    useEffect(() => {
        async function updateData() {
            const data = await getModel(id)
            setData(data)
        }
        updateData()
    }, [id])
    return <div className='body'>
        <SideBar />
        <MainContent>
            { data ? selectModel(id, data) : <div>Buscando os dados...</div> }
        </MainContent>
    </div>
}

export default Model;