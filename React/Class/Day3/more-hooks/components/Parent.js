import Child from "./Child";

const Parent = (props) => {
    return (
        <>
            <h2>Child</h2>
            <Child fromapp = {props.fromapp} setText={props.setText}/>
        </>
    );
};

export default Parent;