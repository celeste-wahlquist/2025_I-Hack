import PropTypes from 'prop-types';
import ShopItem from './ShopItem';
import {createUser, getUser} from './firebase_stuff/Data';


// props = list of items to buy with weather they are in pantry or not
// shop list should come in as name / value
function ShoppingList(){
    // props.shopList
    const shopItemsSmall = [ {name: "chicken breast", inPantry: "Low"},
                        {name: "tumeric", inPantry: "Yes"},
                        {name: "salt", inPantry: "Yes"},
                        {name: "parsley", inPantry: "No"},
                        {name: "chives", inPantry: "No"},

    ]
    const shopList = shopItemsSmall.map(item => ShopItem(item))
    return (
        <div className = "ShoppingList">
            <div>
                <h2>Shopping List</h2>
                <hr />
            </div>
            <button onClick={createUser}>This button!</button>
            <div>
                <ul>                  
                    {shopList}
                </ul>
            </div>
        </div>
    )
}
export default ShoppingList
// ShoppingList.PropTypes = {
//     shopList: propTypes. , 
//     inPantry: PropTypes.oneOf([Yes,No,Low]).isRequired,
// }