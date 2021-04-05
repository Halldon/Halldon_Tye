import React from 'react';
import { Link } from 'react-router-dom';
import axios from "axios";

import './Models.css'

const baseUrl = 'http://localhost:5000';
const GET_MODELS_URL = `${baseUrl}/models`;

export const Models = () => {
    const [models, setModels] = React.useState([]);

    React.useEffect(() => {
        axios
            .get(GET_MODELS_URL)
            .then(
                ({data: data}) => {
                    setModels(data);
                }
            );
    }, []);

    return (
        <div className="Models">
            <h1>Available Models:</h1>
            {models.map(id => (
                <Link className="model-link" to={`/models/${id}`} key={id}>{id}</Link>
            ))}
        </div>
    )
}