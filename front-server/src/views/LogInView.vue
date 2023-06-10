<template>
   <div class="container">
    <h1>Login Page</h1>
    <hr>
    <form @submit.prevent="login">
      <div class="mb-3" :class="{ 'has-error': usernameError }">
        <label for="exampleInputEmail1" class="form-label">이름</label>
        <input type="text" class="form-control" id="username" aria-describedby="emailHelp" v-model="username">
        <div v-if="usernameError" class="error-message">이름을 입력해주세요.</div>
      </div>
      <div class="mb-3" :class="{ 'has-error': passwordError }">
        <label for="password" class="form-label">비밀번호</label>
        <input type="password" class="form-control" id="password" v-model="password">
        <div v-if="passwordError" class="error-message">비밀번호를 입력해주세요.</div>
      </div>
      <hr>
      <button type="submit" class="btn btn-primary">login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      usernameError: false,
      passwordError: false,
    }
  },
  methods: {
    login() {

      this.clearErrors();
      if (!this.username) {
        this.usernameError = true;
      }
      if (!this.password) {
        this.passwordError = true;
      }

      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    },

    clearErrors() {
      this.usernameError = false;
      this.passwordError = false;
    }
  }
}
</script>

<style>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-label {
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-primary {
  display: block;
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.has-error .form-control {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 12px;
  margin-top: 5px;
}

</style>
