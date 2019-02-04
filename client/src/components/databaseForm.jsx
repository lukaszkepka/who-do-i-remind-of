import React from "react";

export default class DataBaseForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: this.props.dataBases[0].id };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    this.props.onDataBaseSubmit(this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <>
        <div className="form-title">Choose Your Favourite Group</div>
        <form onSubmit={this.handleSubmit}>
          <div className="base-picker">
            <div>{"<"}</div>
            <div>{this.props.dataBases[this.state.value].name}</div>
            <div>{">"}</div>
          </div>
          <select value={this.state.value} onChange={this.handleChange}>
            {this.props.dataBases.map(base => (
              <option value={base.id}>{base.name}</option>
            ))}
          </select>
          <div>
            Description:
            <p>{this.props.dataBases[this.state.value].description}</p>
          </div>
          <div>
            <p>
              {this.props.dataBases[this.state.value].photos.map(photo => (
                <img height="100" width="100" src={photo} />
              ))}
            </p>
          </div>
          <div>
            <input type="submit" value="Next Section" />
          </div>
        </form>
      </>
    );
  }
}
