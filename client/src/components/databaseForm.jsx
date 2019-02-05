import React from "react";

export default class DataBaseForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      index: 0
    };

    this.handleNextClick = this.handleNextClick.bind(this);
    this.handlePreviousClick = this.handlePreviousClick.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleNextClick() {
    this.setState({ index: (this.state.index + 1) % this.props.dataBases.length });
  }

  handlePreviousClick() {
    this.setState({ index: this.state.index > 0 ? this.state.index - 1 : this.props.dataBases.length - 1});
  }

  handleSubmit(event) {
    this.props.onDataBaseSubmit(this.props.dataBases[this.state.index]);
    event.preventDefault();
  }

  render() {
    return (
      <>
        <div className="form-title">Choose Your Favourite Group</div>
        <form onSubmit={this.handleSubmit}>
          <div className="base-picker">
            <input className="arrow-button" type="button" value="<" onClick={this.handlePreviousClick}/>
            <div className="base-name">{this.props.dataBases[this.state.index].name}</div>
            <input className="arrow-button" type="button" value=">" onClick={this.handleNextClick} />
          </div>
          {/* <select value={this.state.value} onChange={this.handleChange}>
            {this.props.dataBases.map(base => (
              <option value={base.id}>{base.name}</option>
            ))}
          </select> */}
          <div>
            <p className="base-description">{this.props.dataBases[this.state.index].description}</p>
          </div>
          <div className="photos">
            {/* <div>A few celebrities among this group</div> */}
            {this.props.dataBases[this.state.index].photos.map(photo => (
              <img src={photo} />
            ))}
          </div>
          <div>
            <input type="submit" value="Next Section" />
          </div>
        </form>
      </>
    );
  }
}
