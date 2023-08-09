import SubChild from "./SubChild";

const Child = (props) => {
    return (
        <>
            <h2>Child</h2>
            <SubChild fromapp = {props.fromapp} setText={props.setText}/>
        </>
    );
};

export default Child