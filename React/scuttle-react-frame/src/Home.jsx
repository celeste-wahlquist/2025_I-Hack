import './Home.css';
import logo from './images/logo.png';
import ShoppingList from './components/ShoppingList';
import shelf from './images/shelf.png';
import list from './images/groceryList.png'

function Home() {

    function handlePantryClick() {
        const logo = document.querySelector('.scuttleTitle');
        const shelf = document.getElementById('pantryShelf');
        shelf.classList.toggle('fade-out');
        if (!logo.classList.contains('fade-out')) {
            logo.classList.toggle('fade-out');
        } 
        if (!shelf.classList.contains('fade-out')) {
            logo.classList.add('fade-out');
        }
        else {
            logo.classList.remove('fade-out');
        }
    }
    function handleListClick() {
        const logo = document.querySelector('.scuttleTitle');
        const listContainer = document.getElementById('groceryList');

        listContainer.classList.toggle('fade-out'); 
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
                    <img src={shelf} alt="shelf" id="pantryShelf" className="fade-out" />
                    <div id="groceryList" className="fade-out">
                        <img src={list} alt="list" id="groceryListImage"/>
                        <div className="listData"><ShoppingList/></div>
                    </div>
                </div>
            </header>
        </div>
    );
}
export default Home;