import React from "react";

export default class ErrorPage extends React.Component {
  render() {
    return (
      <div>
        <p>Ops! It seems that there is no face in the picture.</p>
        <p>Try to upload different photo</p>
      </div>
    );
  }
}
