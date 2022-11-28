<template>
    <div class="login-page">
        <img class="Logo" src="../public/logos/Andes_express.png">
        <div class="form">
            <a-form
                :model="formState"
                name="basic"
                :label-col="{ span: 8 }"
                :wrapper-col="{ span: 16 }"
                autocomplete="off"
            >
                <a-form-item
                label="Correo electrónico"
                :rules="[{ required: true, message: 'Please input your username!' }]"
                class="formItem"
                >
                <a-input v-model:value="formState.username" />
                </a-form-item>
  
                <a-form-item
                label="Contraseña"
                :rules="[{ required: true, message: 'Please input your password!' }]"
                class="formItem"
                >
                <a-input-password v-model:value="formState.password" />
                </a-form-item>
  
                <!--<a-form-item name="remember" :wrapper-col="{ offset: 8, span: 16 }">
                <a-checkbox v-model:checked="formState.remember">Remember me</a-checkbox>
                </a-form-item>-->
  
                <p v-if="noIngreso" style="color:red">Datos ingresados incorrectos.</p>
  
                <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
                <a-button type="primary" html-type="submit" @click="iniciarSesion">Iniciar Sesión</a-button>
                </a-form-item>
            </a-form>
        </div>
    </div>
  </template>
  
  <script>
  
  import {getLogin} from '../services/index';
  
  export default {
    components: {
    
    },
    name: "index",
    data() {
        return{ 
            formState:{
                username:'',
                password:'',
            },
            noIngreso:false,
        }
    },
    methods: {
        async iniciarSesion(){
            //this.$router.push('/incidentes');
            console.log(this.formState.username,this.formState.password);
            try{
                let data=await getLogin(this.formState.username,this.formState.password);
                console.log(data);
                if(data.data.id!=null){
                    this.$router.push('/incidentes');
                }else{
                    this.noIngreso=true;
                    setTimeout(()=>{
                        this.noIngreso=false;
                    },5000)
                }
            }catch(err){
                this.noIngreso=true;
                    setTimeout(()=>{
                        this.noIngreso=false;
                    },5000)
                console.log(err);
            }
            
        },
    },
    created(){
        //this.$router.go(-1);
    }
  }
  </script>
  <style>
  .login-page {
          width: 445px;
          padding: 5% 0 0;
          margin: auto;
      }
  
  .formItem{
    
  }
  .Logo{
    position: relative;
    width: 400px;
    height: 80px;
  }
  </style>