<template>
  <div class="principal">
    <h1>{{ msg }}</h1>
    <div class="container">
    <form @submit="formSubmit">
      <label for="A">Quantidade de maçãs em cada árvore</label><input type="text" placeholder="Use a vírgula como separador" required v-model="A" id="A" name="A">
      <label for="K">Marcelo</label><input type="number" placeholder="Árvores consecutivas" required v-model="K" id="K" name="K">
      <label for="L">Carla</label><input type="number" placeholder="Árvores consecutivas" required id="L" v-model="L" name="L">
      
      <button type="submit">Calcular</button>
    </form>
    <label for="qtd">Quantidade máxima de maçãs</label><span class="qtd">{{dados.qtd_macas}}</span>
    </div>
    <div class="rodape">
    <footer>
    <a href="http://localhost:5000/docs" target="_blank">Documentação da API</a>
  </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

let scopoDados = null;
export default {
  name: 'Dados',
  props: {
    msg: String
  },
  mounted(){
    console.log('Component mounted.')
  },
  data() {
    return {
      dados: [],
      A: '',
      K: '',
      L: '',
      output: ''
    }
  },
  methods: {
    mostrar: () => {
      axios.get(`http://localhost:5000/tree`).then(res=>{
        console.log(res)
        scopoDados.dados = res.data
      })
    },
    formSubmit(e){
      e.preventDefault();
      let currentObj = this;
      this.axios.post('http://localhost:5000/tree', {
        A: this.A,
        K: this.K,
        L: this.L
      })
      .then(function(response){
        currentObj.output = response.data;
      })
      .then(()=>{
        this.mostrar()
      })
      .catch(error =>{
        currentObj.output = error;
      });
    },
    validarList(){
      var inputA = document.getElementById("A")
      inputA.addEventListener('click', ()=>{
        window.alert('sometext')
      })
    }
  },
  created() {
    scopoDados = this;
    this.mostrar()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style>

body{
  width: 100%;
  margin: 0;
  padding: 0;
  font-family: 'Courier New', Courier, monospace;
  background: rgb(243, 243, 243);
}

.container{
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

form{
  margin: 20px 0;
  background-color: white;
  padding: 30px 25px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 36%;
}

label{
  font-size: 16px;
  color: darkslateblue;
}

input{
  width: 100%;
  display: block;
  margin-top: 8px;
  margin-left: 0;
  padding: 7px;
  font-size: 16px;
  color: #7159c1;
  border-radius: 2px;
  border: 1px solid #ccddef;
  outline-color: #7159c1;
  height: 20px;
  margin-bottom: 8px;
  text-align: center;
}

button{
  display: block;
  min-width: 120px;
  border: none;
  color: gray;
  border-radius: 25px;
  margin: auto;
  padding: 7px;
  margin-top: 15px;
}

h1{
  display: flex;
  align-items: center;
  justify-content: center;
}

.qtd{
  width: 36%;
  font-size: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

span{
  display: block;
  margin-left: 0;
  padding: 7px;
  font-size: 16px;
  color: #7159c1;
  border-radius: 2px;
  border: 1px solid #ccddef;
  outline-color: #7159c1;
  height: 100%;
  margin-bottom: 8px;
}

.rodape{
  width: 100%;
}

.rodape footer a{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: end;
}

a{
  color: rgb(104, 104, 104);
}

</style>