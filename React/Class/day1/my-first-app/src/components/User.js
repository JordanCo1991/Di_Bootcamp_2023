import "./User.css";

const User = (props) => {
    const {userinfo} = props;


    const styling = {
        display:'inline-block',
        textAlign: 'center',
        padding: '20px',
        margin: '20px',
        border: '1px solid #ccc',
        borderRadius: '15px',
    }
    return (
        <div
         className="userstyle">
            
            <img src={`https://robohash.org/${userinfo.id}?size=150x150`} alt=''/>
            <h2>{userinfo.name}</h2>
            <h4>{userinfo.email}</h4>
            <p>{userinfo.usernames}</p>
        </div>
    )
}
export default User