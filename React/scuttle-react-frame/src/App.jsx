import './App.css';
import logo from './images/logo.png'
import ShoppingList from './ShoppingList';
import shelf from './images/shelf.png';

function App() {
    function handlePantryClick() {
        
    }
    
    
    
    
  return (
    <div className="App">
      <header className="App-hero">
          <div className="navBar">
              <button className="navButton" onClick={}>Pantry</button>
              <button className="navButton"></button>
          </div>
          <img src={logo} className="scuttleTitle" alt="logo" />
          {/*<img src={shelf} alt="shelf" id="pantryShelf"/>*/}
          <div>
              {/*<ShoppingList />*/}
          </div>
      </header>
    </div>
  );
}



export default App;
