import PropTypes from 'prop-types'
function Pantry(props) {
    
    const renderIngredients = <h2 className="ingredient">
                                        {ingredientName}
                                        {ingredientQuantity}
                                        </h2>
    const pantryIsEmpty = <h2 className="emptyPantry">
                                    Pantry is empty
                                    </h2>
    return(props.hasIngredients ? renderIngredients : pantryIsEmpty)
}
export default Pantry