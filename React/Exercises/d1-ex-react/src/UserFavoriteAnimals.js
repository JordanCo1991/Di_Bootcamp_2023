const UserFavoriteAnimals = (props) => {
    return(
        <>
        <p>test</p>
        <ul>
            {props.animals.map((animal,index) => 
             <li key= {index}> {animal}</li>
            )}
        </ul>
        </>
    )
}



export default UserFavoriteAnimals;