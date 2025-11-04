import PropTypes from 'prop-types';
// prop = is in pantry, name
function ShopItem(props)
{
    const inPantry = <li className = "in-pantry">{props.name}</li>
    const low = <li className = "low">{props.name}</li>
    const pleaseBuy = <li className = "please-buy">{props.name}</li>
    
    const lookup = {//this look up statement brought to you by ChatGPT when cleaning up an if statement
        Yes: inPantry,
        Low: low,
        };

    return lookup[props.isInPantry] ?? pleaseBuy;//also this return syntax with the look up
}
ShopItem.propTypes = {
    isInPantry: PropTypes.oneOf(['Yes', 'No', 'Low']).isRequired,
    name: PropTypes.string,
}

export default ShopItem