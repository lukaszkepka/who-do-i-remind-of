import React from "react";
import xService from "../services/xService";
import Loader from "./loader";
export default class AllResults extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      results: []
    };
    this.service = new xService();
    this.handleReset = this.handleReset.bind(this);
    this.handleBack = this.handleBack.bind(this);
  }

  componentDidMount() {
    console.log("fetching...");
    this.service
      .getAllResults()
      .then(response =>
        this.setState({ results: [...response], isLoading: false })
      );
  }

  handleReset() {
    this.props.onResetClick();
  }

  handleBack() {
    this.props.onBackClick();
  }

  render() {
    if (this.state.isLoading) {
      return <Loader />;
    }
    return (
      <>
        <div className="result-rows">
          {this.state.results.map((result, i) => (
            <div className="result-row" key={i}>
              <div className="user-name">{result.userName} </div>
              <div> reminds me of </div>
              <div>{result.celebrityName}</div>
              <img src={result.celebrityPhoto} />
              <div className="match-ratio-value">
                {(result.ratio * 100).toFixed()}%
              </div>
            </div>
          ))}
        </div>
        <input type="button" value="Try another photo" onClick={this.handleReset} />
        <input type="button" value="Back" onClick={this.handleBack} />
      </>
    );
  }
}
