import React, { useState } from "react";
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import AppBar from "./appBar";

function Login(props) {
    const [username, setUserName] = useState("")
    const [password, setPassword] = useState("")

    function validateUsername() {
        let message = ""

        if (username.length > 10) message = "Username bigger"

        return message
    }

    function validatePassword() {
        let message = ""

        if (password.length < 5) message = "Password smaller"

        return message
    }

    function getErrors() {
        const errors = []
        errors[0] = validateUsername()
        errors[1] = validatePassword()

        return errors
    }

    const errors = getErrors()

    const hasErrors = errors.some((item) => item !== "")

    return (
        <>
            <AppBar />
            <Paper elevation={3} sx={{display: "flex", flexDirection: "column", gap: "10px", padding: "10px", width: "50%"}}>
                <TextField 
                    id="outlined-basic" 
                    label="Outlined" 
                    variant="outlined" 
                    value={username} 
                    onChange = {(e) => setUserName(e.target.value)}
                    helperText={errors[0]}
                    error={errors[0] !== ""}
                />
                <TextField
                    id="outlined-password-input"
                    label="Password"
                    type="password"
                    autoComplete="current-password"
                    value={password}
                    onChange = {(e) => setPassword(e.target.value)}
                    helperText={errors[1]}
                    error={errors[1] !== ""}
                />
                <Button variant="outlined" disabled = {hasErrors}>Login</Button>
            </Paper>
        </>
    )
}

export default Login