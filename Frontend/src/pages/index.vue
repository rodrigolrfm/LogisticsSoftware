<template>
    <div class="foto">
    <div class="login-page" >
        <img class="Logo" src="../public/logos/Andes_express.png">
        <div class="form">
            <a-form
                :model="formState"
                name="basic"
                :label-col="{ span: 8 }"
                :wrapper-col="{ span: 16 }"
                autocomplete="off"
            >
                <p class="textoBienvenida">Bienvenido a Andes Express</p>
                <a-form-item
                label="Correo electrónico"
                :rules="[{ required: true, message: 'Please input your username!' }]"
                class="formItem"
                >
                <a-input v-model:value="formState.username" class="inputs" />
                </a-form-item>
  
                <a-form-item
                label="Contraseña"
                :rules="[{ required: true, message: 'Please input your password!' }]"
                class="formItem"
                >
                <a-input-password v-model:value="formState.password" class="inputs" />
                </a-form-item>
  
                <a-form-item name="remember" :wrapper-col="{ offset: 8, span: 16 }">
                <a-checkbox v-model:checked="formState.remember">Recuérdame</a-checkbox>
                </a-form-item>
  
                <p v-if="noIngreso" style="color:red">Datos ingresados incorrectos.</p>
                
                <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
                <a-button type="primary" html-type="submit" @click="iniciarSesion">Iniciar Sesión</a-button>
                </a-form-item>
                <p class="textoCrearCuenta">¿No tienes una cuenta? <span style="color:#FF0000">Crea una aquí</span></p>
  
                <img class="loginGoogle" src="../public/logos/loginGoogle.png">
  
                <p style="color:#FFFFFF">_</p>
            </a-form>
        </div>
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
  .loginGoogle{
    margin-left: 100px;
    height: 60px;
    width: 300px;
  }
  .textoCrearCuenta{
    font-size: 12px;
    text-align: center;
    font-weight: 100;
  }
  .textoBienvenida{
    font-size: 18px;
    text-align: center;
    font-weight: 800;
  }
  .login-page {
    width: 500px;
    margin: auto;
    background-color: white;
  }
  .foto{
    background: url(../public/logos/fotoFondo.png);
    height: 650px;
    padding-top: 100px;
  }
  .inputs{
    width: 300px;
  }
  .Logo{
    margin-left: 50px;
    width: 400px;
    height: 80px;
  }
  </style>