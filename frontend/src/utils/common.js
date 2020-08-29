import axios from 'axios'

axios.defaults.withCredentials = true   // 这句代码代表每次发送请求，都把cookie带上

//后端的域名
const backendHost = "http://192.168.123.183:8001/api/"


export const postRequest = function (path, data={}) {
    return axios.post(backendHost + path, data)
}

export const putRequest = function (path, data={}) {
    return axios.put(backendHost + path, data)
}

export const deleteRequest = function (path, data={}) {
    return axios.delete(backendHost + path, data)
}

export const patchRequest = function (path, data={}) {
    return axios.patch(backendHost + path, data)
}

export const getRequest = function (path, data={}) {
    return axios.get(backendHost + path, {
        params:data
    })
}