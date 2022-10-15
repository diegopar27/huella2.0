<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    prepend-icon=""
                    name="login"
                    label="Login"
                    type="text"
                    v-model="value1"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    prepend-icon=""
                    v-model="value2"
                    name="password"
                    label="Password"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login()" to="/">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      value1: "",
      value2: "",
      colorx: "#c72a75",
      colorx2: "#5252e8",
    };
  },
  methods: {
    ...mapActions({
      LOGIN: "usuario/loginUsuario",
      GETHISTORIAS: "usuario/gethistorias",
    }),
    async login() {
      console.log("LOGIN");
      let data = {
        usuario: this.value1,
        password: this.value2,
      };
      let res = await this.LOGIN({ data });
      console.log(res);
      if (res) {
        sessionStorage.usuario = JSON.stringify(res);
        return this.$router.push("/");
      }
    },
  },
  created() {
    this.GETHISTORIAS();
  },
};
</script>

<style></style>
