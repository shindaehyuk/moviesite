<template>
  <div class="container">
    <h1>Sign Up Page</h1>
    <hr>
    <form @submit.prevent="signUp">
      <div class="mb-3" :class="{ 'has-error': usernameError }">
        <label for="username" class="form-label">이름</label>
        <input type="text" class="form-control" id="username" v-model="username">
        <div v-if="usernameError" class="error-message">이름을 입력해주세요.</div>
      </div>
      <div class="mb-3" :class="{ 'has-error': password1Error }">
        <label for="password1" class="form-label">비밀번호</label>
        <input type="password" class="form-control" id="password1" v-model="password1">
        <div v-if="password1Error" class="error-message">비밀번호를 입력해주세요.</div>
      </div>
      <div class="mb-3" :class="{ 'has-error': password2Error }">
        <label for="password2" class="form-label">비밀번호 확인</label>
        <input type="password" class="form-control" id="password2" v-model="password2">
        <div v-if="password2Error" class="error-message">비밀번호 확인을 입력해주세요.</div>
      </div>

      <hr>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      usernameError: false,
      password1Error: false,
      password2Error: false,
      }
  },
  methods: {
    signUp() {
      this.clearErrors();

      if (!this.username) {
        this.usernameError = true;
      }
      if (!this.password1) {
        this.password1Error = true;
      }
      if (!this.password2) {
        this.password2Error = true;
      }

      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    },
    clearErrors() {
      this.usernameError = false;
      this.password1Error = false;
      this.password2Error = false;
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
