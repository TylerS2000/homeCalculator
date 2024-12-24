import React, { useState } from "react";

export default function Calculator(props) {
    const [homePriceState, setHomePriceState] = useState(0);
    const [downPaymentState, setDownPaymentState] = useState(0);
    const [interestRateState, setInterestRateState] = useState(0);

    const inputs = [{title:"Home Price", id:"homePrice", value:homePriceState, setState:setHomePriceState},
        {title:"Down Payment", id:"downPayment", value:downPaymentState, setState:setDownPaymentState},
        {title:"Interest Rate", id:"interestRate", value:interestRateState, setState:setInterestRateState}]

    function handleChange(event, setStateFunction){
        setStateFunction(event.target.value)
        console.log(event.target.value)
    }

    const inputsMap = inputs.map((input)=><div><label for={input.id}>{input.title}</label><input id={input.id} onChange={(e)=>handleChange(e,input.setState)}/></div>)

    return (
        inputsMap
    )
}
