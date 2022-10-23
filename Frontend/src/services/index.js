import axios from 'axios';

const URL="http://localhost:8080";
axios.defaults.withCredentials=true;

export function getSugerencia(file){
    return axios.post(URL+"/uploadfile",{
        "file":file,
    });
}