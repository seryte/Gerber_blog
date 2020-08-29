import {deleteRequest, getRequest, postRequest} from "./common";

export const register = function (username, password, email) {
    return postRequest("user/register/", {
        username: username,
        password: password,
        email: email
    })
}

export const login = function (username, password) {
    return postRequest("user/login/", {
        username: username,
        password: password
    })

}

export const logout = function () {
    return deleteRequest("user/logout/")

}

export const getLoginUserInfo = function () {
    return getRequest("user/info/")
}