<script setup>
import { ref, computed } from "vue";

const produtos = ref([
  { id: 1, nome: "Livro de Vue.js", preco: 79.9 },
  { id: 2, nome: "Curso de Vite", preco: 120.5 },
  { id: 3, nome: "Template HTML Premium", preco: 99.0 },
  { id: 4, nome: "E-book de CSS Moderno", preco: 45.0 },
]);

function finalizarCompra() {
  alert("Compra finalizada com sucesso!");
  carrinho.value = [];
}

const carrinho = ref([]);

function adicionarAoCarrinho(produto) {
  carrinho.value.push(produto);
}

const totalCarrinho = computed(() => {
  return carrinho.value.reduce((total, item) => total + item.preco, 0);
});
</script>

<template>
  <div id="loja-virtual">
    <header class="loja-header">
      <h1>Minha Loja Vue</h1>
      <p>Exercício - Venda de Produtos</p>
    </header>

    <main class="conteudo-principal">
      <section class="produtos-container">
        <h2>Produtos Disponíveis</h2>
        <div class="lista-produtos">
          <div
            v-for="produto in produtos"
            :key="produto.id"
            class="produto-item"
          >
            <p>{{ produto.nome }}</p>
            <p class="preco">R$ {{ produto.preco.toFixed(2) }}</p>
            <button @click="adicionarAoCarrinho(produto)">
              Adicionar ao Carrinho
            </button>
          </div>
        </div>
      </section>

      <section class="carrinho-container" v-if="carrinho.length > 0">
        <h2>Seu Carrinho de Compras</h2>
        <div class="lista-carrinho">
          <div
            v-for="(item, index) in carrinho"
            :key="index"
            class="carrinho-item"
          >
            <span>{{ item.nome }}</span>
            <span>R$ {{ item.preco.toFixed(2) }}</span>
          </div>
        </div>
        <hr />
        <div class="total-carrinho">
          <h3>Total: R$ {{ totalCarrinho.toFixed(2) }}</h3>
        </div>

        <div class="aviso-frete" v-show="totalCarrinho > 200">
          Parabéns! Você tem direito a frete grátis!
        </div>

        <div class="opcoes-pagamento">
          <h4>Finalizar Compra</h4>
          <button class="btn-pagamento" @click="finalizarCompra">
            Ir para Pagamento
          </button>
        </div>
      </section>

      <section class="carrinho-vazio" v-if="carrinho.length === 0">
        <p>O seu carrinho está vazio.</p>
      </section>
    </main>
  </div>
</template>

<style scoped>
/* Estilos para a aplicação */
#loja-virtual {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.loja-header {
  text-align: center;
  margin-bottom: 40px;
  border-bottom: 1px solid #eee;
  padding-bottom: 20px;
}

.produtos-container h2,
.carrinho-container h2 {
  margin-bottom: 20px;
}

.lista-produtos {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.produto-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.produto-item .preco {
  font-weight: bold;
  color: #42b983;
  margin: 10px 0;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

button:hover {
  background-color: #33a06f;
}

.carrinho-container {
  margin-top: 40px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.carrinho-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.total-carrinho {
  text-align: right;
  margin-top: 20px;
  font-size: 1.2em;
}

.aviso-frete {
  text-align: center;
  margin-top: 15px;
  color: #28a745;
  font-weight: bold;
}

.opcoes-pagamento {
  margin-top: 20px;
  text-align: center;
}

.btn-pagamento {
  background-color: #007bff;
  padding: 12px 25px;
  font-size: 16px;
}
.btn-pagamento:hover {
  background-color: #0056b3;
}

.carrinho-vazio {
  text-align: center;
  margin-top: 40px;
  padding: 20px;
  background-color: #fafafa;
  color: #888;
}
</style>
