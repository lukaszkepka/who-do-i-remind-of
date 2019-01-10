import React from "react";
import xService from "../services/xService";

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
      return <div>Loading...</div>;
    }
    return (
      <div>
        {this.state.results.map((result, i) => (
          <div key={i}>
            {`${result.userName} reminds me of ${result.celebrityName}`}
            <img height="50" width="50" src={result.celebrityPhoto} />
            {`in ${(result.ratio * 100).toFixed()}%`}
          </div>
        ))}
        <input type="button" value="Reset" onClick={this.handleReset} />
        <input type="button" value="Back" onClick={this.handleBack} />
      </div>
    );
  }
}
