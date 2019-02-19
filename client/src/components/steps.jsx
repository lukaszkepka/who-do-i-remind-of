import React from "react";
// import imggg from "../assets/trianglify.png";
export default class StepProgressBar extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className="container">
        <div className="steps">
          <div className={`step step-name-icon ${this.props.currentStep >= 0 ? "active" : ""}`}>1</div>
          <div className="progressbar progressbar1">
            <div
              className={`innerbar ${this.props.currentStep >= 1 ? "max" : ""}`}
            />
          </div>
          <div className={`step step-photo-icon non-first-step ${this.props.currentStep >= 1 ? "active" : ""}`}>2</div>
          <div className="progressbar progressbar2">
            <div
              className={`innerbar ${this.props.currentStep >= 2 ? "max" : ""}`}
            />
          </div>
          <div className={`step step-database-icon non-first-step ${this.props.currentStep >= 2 ? "active" : ""}`}>3</div>
          <div className="step-name">About</div>
          <div className="step-photo">Celebrities</div>
          <div className="step-database">Photo</div>
        </div>
      </div>
    );
  }
}
