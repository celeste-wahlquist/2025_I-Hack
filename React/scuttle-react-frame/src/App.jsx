import logo from './logo.svg';
import './App.css';
import ShoppingList from './ShoppingList';
import MealIndiv from './MealIndiv';
import foodwave from './images/foodwavecropped.png';
import MealPlan from './MealPlan'


function App() {
  const mealList = [['ceaeal', '0', '0'], ['PB+J', '0', '5'], ['Pot Roast', '240', '120']]
 
  return (
    <div className="App">
      <header className="App-header">
        <ShoppingList />
        <p>Hi</p>  
        <MealIndiv
                  timeOfMeal="B"
                  mealName="Empty"
                  cookTime = "50"
                  prepTime = "90"
        />
        <MealPlan
                day = "sat"
                allMeals = {mealList}
        />
        <img src={foodwave} alt="foodwave" id="heroImage" />
      </header>
        <Pantry hasIngredients={true}/>
    </div>
  );
}

export default App;
