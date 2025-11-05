import logo from './logo.svg';
import './App.css';
import ShoppingList from './ShoppingList';
import foodwave from './images/foodwavecropped.png';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ShoppingList />
        <p>Hi</p>
        
        <img src={foodwave} alt="foodwave" id="heroImage" />
      </header>
    </div>
  );
}

export default App;
