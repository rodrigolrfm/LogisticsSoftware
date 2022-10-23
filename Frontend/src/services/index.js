import axios from 'axios';

const URL="http://localhost:8000";
axios.defaults.withCredentials=true;

export function getSugerencia(file){
    console.log(file)
    return axios.post(URL+"/general/uploadfile/",{
        "file":file,
    });
}