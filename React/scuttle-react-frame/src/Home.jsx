import './Home.css';
import logo from './images/logo.png';
import ShoppingList from './ShoppingList';
import shelf from './images/shelf.png';
import list from './images/groceryList.png'

function Home() {

    function handlePantryClick() {
        const logo = document.querySelector('.scuttleTitle');
        const shelf = document.getElementById('pantryShelf');
        logo.classList.toggle('fade-out');
        shelf.classList.toggle('fade-out');
    }
    
    function handleListClick() {
        const list = document.getElementById('groceryList')
        list.classList.toggle('fade-out');
    }
    
    
    return (
        <div className="Home">

            <header className="Home-hero">
                <div className="navBar">
                    <button className="navButton" onClick={handlePantryClick}>Pantry</button>
                    <button className="navButton">Recipe Book</button>
                    <button className="navButton" onClick={handleListClick}>Shopping List</button>
                    <button className="navButton">Meal Plan</button>
                    <button className="navButton">Login</button>
                </div>
                <img src={logo} className="scuttleTitle" alt="logo"/>
                <div className="scuttleTasks">
                    <ShoppingList />
                    <img src={shelf} alt="shelf" id="pantryShelf" className="fade-out" />
                    <img src={list} alt="list" id="groceryList" className="fade-out"/>
                </div>
            </header>
        </div>
    );
}
export default Home;