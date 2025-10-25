import MealIndiv from './MealIndiv'
import React, {useState} from 'react';



function MealPlan({day, allMeals})
{
    const [meals, setMeals] = useState(allMeals);
    const mealTimes = ['B', 'L', 'D'];

    const editMeal = (index) => {
        setMeals(prevMeals => {
            const updatedMeals = [...prevMeals];
            updatedMeals[index] = 2;//search();
            return updatedMeals;
        });
    }

    return(
        <div>
            <h2><b>{day}</b></h2>
            {meals.map((meal, index) => (
                <div key={index}>
                    <MealIndiv
                        timeOfMeal={mealTimes[index]}
                        mealName={meal?.[0]}
                        cookTime={meal?.[1]}
                        prepTime={meal?.[2]}
                    />
                    <button onClick={() => editMeal(index)}>
                        Edit    
                    </button>
                </div>
            ))}
        </div>
    )
}

export default MealPlan