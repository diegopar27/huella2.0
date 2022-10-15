import http from "@/http";

export default {
    namespaced: true,
    state: {
        usuario: null,
    },
    getters: {
    },
    mutations: {
    },
    actions: {
        async loginUsuario({ commit }, { data }) {
            const { usuario, password } = data

            try {
                const respuesta = await http({
                    url: `user/lista`,
                    header: {},
                    method: "GET",

                });
                let acceso = {}
                respuesta.forEach(e => {
                    if (usuario == e.name && password == e.password) acceso = e
                    else acceso = 400
                });
                return acceso


            } catch (error) {
                console.error(error);
            }
        },
        async gethistorias({ commit }) {
            try {
                const respuesta = await http({
                    url: `historia/lista`,
                    header: {},
                    method: "GET",

                });
                console.log(respuesta)
                return respuesta

            } catch (error) {
                console.error(error);
            }
        },
    },
};