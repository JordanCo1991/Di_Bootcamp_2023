const SubChild = (props) => {
    return (
        <>
            <h2>Sub Child</h2>
            Props: {props.fromapp}
            <div>
                <button onClick={()=>props.setText('Bla Bla Bla')}>Change text</button>
            </div>
        </>
    );
};

export default SubChild