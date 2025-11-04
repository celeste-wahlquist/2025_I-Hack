import PropTypes from 'prop-types';


function MealIndiv ({timeOfMeal, mealName="Empty", cookTime=0, prepTime=0})
{
    function TimeToDone(minutes){
        const mins = minutes % 60;
        const hours = (minutes - mins) / 60;
        return(
            <p>{(hours === 0) ? "" : hours+"hr" } {(mins === 0) ? "" : mins+"mins" }</p>    
        )
    }
    
    return(
        <div>
            <aside>
                <h1>{timeOfMeal}</h1>
            </aside>
            <b><h3>{mealName}</h3></b>
            <p>time to prep: {TimeToDone(parseInt(prepTime))}</p>
            <p>time to cook: {TimeToDone(parseInt(cookTime))}</p>
           
        </div>
    )
}
MealIndiv.propTypes = {
    mealName: PropTypes.oneOf(['B', 'L', 'D', 'S']).isRequired,
    cookTime: PropTypes.string,
    prepTime: PropTypes.string,
}
export default MealIndiv