import React from "react";
import ResultSlider from "./resultSlider";
import PhotoSlider from "./photoSlider";

export default class ResultPage extends React.Component {
  constructor(props) {
    super(props);

    this.handleReset = this.handleReset.bind(this);
    this.handleShowAllResults = this.handleShowAllResults.bind(this);
  }

  handleReset() {
    this.props.onResetClick();
  }

  handleShowAllResults() {
    this.props.onShowAllResultsClick();
  }

  render() {
    return (
      <div>
        <div className="flex">
          <div className="flex vertical">
            <img height="200" width="200" src={this.props.userPhoto} />
            {this.props.userName}
          </div>
          reminds me of
          <PhotoSlider />
          {/* <ResultSlider results={this.props.similarPeople} /> */}
        </div>
        <input type="button" value="Try another photo" onClick={this.handleReset} />
        <input
          type="button"
          value="Show other people results"
          onClick={this.handleShowAllResults}
        />
      </div>
    );
  }
}
