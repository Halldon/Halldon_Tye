import React from "react";
import { Form, Button, Row, Col } from "react-bootstrap";
import axios from "axios";
import { debounce } from "lodash";
import { useParams } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";

const baseUrl = 'http://localhost:5000';
const UI_PARAMS_API_URL = (modelId) => `${baseUrl}/models/${modelId}/params`;
const TRANSLATE_API_URL = (modelId) => `${baseUrl}/models/${modelId}/translate`;
const EXAMPLE_API_URL = (modelId) => `${baseUrl}/models/${modelId}/examples`;

const DEBOUNCE_INPUT = 250;

const updateExample = (modelId, id, body) => {
  axios.put(`${EXAMPLE_API_URL(modelId)}/${id}`, body);
}

const debouncedUpdateExample = debounce(updateExample, DEBOUNCE_INPUT);

export const ModelForm = () => {
  const { modelId } = useParams();
  const [output, setOutput] = React.useState("");
  const [input, setInput] = React.useState("");
  const [buttonText, setButtonText] = React.useState("Submit");
  const [description, setDescription] = React.useState("Description");
  const [showExampleForm, setShowExampleForm] = React.useState(false);
  const [examples, setExamples] = React.useState({});

  React.useEffect(() => {
    axios
      .get(UI_PARAMS_API_URL(modelId))
      .then(
        ({
          data: { placeholder, button_text, description, show_example_form }
        }) => {
          setInput(placeholder);
          setButtonText(button_text);
          setDescription(description);
          setShowExampleForm(show_example_form);
          if (showExampleForm) {
            axios.get(EXAMPLE_API_URL(modelId)).then(({ data: examples }) => {
              setExamples(examples);
            });
          }
        }
      );
  }, []);

  const handleExampleChange = (id, field) => e => {
    const text = e.target.value;

    let body = { [field]: text };
    examples[id][field] = text;

    setExamples(examples);
    debouncedUpdateExample(modelId, id, body);
  };

  const handleExampleDelete = id => e => {
    e.preventDefault();
    axios.delete(`${EXAMPLE_API_URL(modelId)}/${id}`).then(({ data: examples }) => {
      setExamples(examples);
    });
  };

  const handleExampleAdd = e => {
    e.preventDefault();
    axios.post(EXAMPLE_API_URL(modelId)).then(({ data: examples }) => {
      setExamples(examples);
    });
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  }

  const handleClick = (e) => {
    e.preventDefault();
    const body = {
      prompt: input
    };
    axios.post(TRANSLATE_API_URL(modelId), body).then(({ data: { text } }) => {
      setOutput(text);
    });
  }

  return (
    <div>
      <head />
      <body style={{ alignItems: "center", justifyContent: "center" }}>
        <div
          style={{
            margin: "auto",
            marginTop: "80px",
            display: "block",
            maxWidth: "500px",
            minWidth: "200px",
            width: "50%"
          }}
        >
          <Form onSubmit={handleClick}>
            <Form.Group controlId="formBasicEmail">
              {showExampleForm && (
                <div>
                  <h4 style={{ marginBottom: "25px" }}>Examples</h4>
                  {Object.values(examples).map(example => (
                    <span key={example.id}>
                      <Form.Group
                        as={Row}
                        controlId={"formExampleInput" + example.id}
                      >
                        <Form.Label column="sm" lg={2}>
                          Example Input
                        </Form.Label>
                        <Col sm={10}>
                          <Form.Control
                            type="text"
                            as="input"
                            placeholder="Enter text"
                            value={example.input}
                            onChange={handleExampleChange(
                              example.id,
                              "input"
                            )}
                          />
                        </Col>
                      </Form.Group>
                      <Form.Group
                        as={Row}
                        controlId={"formExampleOutput" + example.id}
                      >
                        <Form.Label column="sm" lg={2}>
                          Example Output
                        </Form.Label>
                        <Col sm={10}>
                          <Form.Control
                            type="text"
                            as="textarea"
                            placeholder="Enter text"
                            value={example.output}
                            onChange={handleExampleChange(
                              example.id,
                              "output"
                            )}
                          />
                        </Col>
                      </Form.Group>
                      <Form.Group as={Row}>
                        <Col sm={{ span: 10, offset: 2 }}>
                          <Button
                            type="button"
                            size="sm"
                            variant="danger"
                            onClick={handleExampleDelete(example.id)}
                          >
                            Delete example
                          </Button>
                        </Col>
                      </Form.Group>
                    </span>
                  ))}
                  <Form.Group as={Row}>
                    <Col sm={{ span: 10 }}>
                      <Button
                        type="button"
                        variant="primary"
                        onClick={handleExampleAdd}
                      >
                        Add example
                      </Button>
                    </Col>
                  </Form.Group>
                </div>
              )}
              <Form.Label>{description}</Form.Label>
              <Form.Control
                type="text"
                as="textarea"
                placeholder="Enter text"
                value={input}
                onChange={handleInputChange}
              />
            </Form.Group>

            <Button variant="primary" type="submit">
              {buttonText}
            </Button>
          </Form>
          <div
            style={{
              textAlign: "center",
              margin: "20px",
              fontSize: "18pt"
            }}
          >
            {output}
          </div>
        </div>
      </body>
    </div>
  );
}


// class
//   App extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       output: "",
//       input: "",
//       buttonText: "Submit",
//       description: "Description",
//       showExampleForm: false,
//       examples: {}
//     };
//     // Bind the event handlers
//     this.handleInputChange = this.handleInputChange.bind(this);
//     this.handleClick = this.handleClick.bind(this);
//   }

//   componentDidMount() {
//     // Call API for the UI params
//     axios
//       .get(UI_PARAMS_API_URL)
//       .then(
//         ({
//           data: { placeholder, button_text, description, show_example_form }
//         }) => {
//           this.setState({
//             input: placeholder,
//             buttonText: button_text,
//             description: description,
//             showExampleForm: show_example_form
//           });
//           if (this.state.showExampleForm) {
//             axios.get(EXAMPLE_API_URL).then(({ data: examples }) => {
//               this.setState({ examples });
//             });
//           }
//         }
//       );
//   }

//   updateExample(id, body) {
//     axios.put(`${EXAMPLE_API_URL}/${id}`, body);
//   }

//   debouncedUpdateExample = debounce(this.updateExample, DEBOUNCE_INPUT);

//   handleExampleChange = (id, field) => e => {
//     const text = e.target.value;

//     let body = { [field]: text };
//     let examples = { ...this.state.examples };
//     examples[id][field] = text;

//     this.setState({ examples });
//     this.debouncedUpdateExample(id, body);
//   };

//   handleExampleDelete = id => e => {
//     e.preventDefault();
//     axios.delete(`${EXAMPLE_API_URL}/${id}`).then(({ data: examples }) => {
//       this.setState({ examples });
//     });
//   };

//   handleExampleAdd = e => {
//     e.preventDefault();
//     axios.post(EXAMPLE_API_URL).then(({ data: examples }) => {
//       this.setState({ examples });
//     });
//   };

//   handleInputChange(e) {
//     this.setState({ input: e.target.value });
//   }

//   handleClick(e) {
//     e.preventDefault();
//     let body = {
//       prompt: this.state.input
//     };
//     axios.post(TRANSLATE_API_URL, body).then(({ data: { text } }) => {
//       this.setState({ output: text });
//     });
//   }

//   render() {
//     const showExampleForm = this.state.showExampleForm;
//     return (
//       <div>
//         <head />
//         <body style={{ alignItems: "center", justifyContent: "center" }}>
//           <div
//             style={{
//               margin: "auto",
//               marginTop: "80px",
//               display: "block",
//               maxWidth: "500px",
//               minWidth: "200px",
//               width: "50%"
//             }}
//           >
//             <Form onSubmit={this.handleClick}>
//               <Form.Group controlId="formBasicEmail">
//                 {showExampleForm && (
//                   <div>
//                     <h4 style={{ marginBottom: "25px" }}>Examples</h4>
//                     {Object.values(this.state.examples).map(example => (
//                       <span key={example.id}>
//                         <Form.Group
//                           as={Row}
//                           controlId={"formExampleInput" + example.id}
//                         >
//                           <Form.Label column="sm" lg={2}>
//                             Example Input
//                           </Form.Label>
//                           <Col sm={10}>
//                             <Form.Control
//                               type="text"
//                               as="input"
//                               placeholder="Enter text"
//                               value={example.input}
//                               onChange={this.handleExampleChange(
//                                 example.id,
//                                 "input"
//                               )}
//                             />
//                           </Col>
//                         </Form.Group>
//                         <Form.Group
//                           as={Row}
//                           controlId={"formExampleOutput" + example.id}
//                         >
//                           <Form.Label column="sm" lg={2}>
//                             Example Output
//                           </Form.Label>
//                           <Col sm={10}>
//                             <Form.Control
//                               type="text"
//                               as="textarea"
//                               placeholder="Enter text"
//                               value={example.output}
//                               onChange={this.handleExampleChange(
//                                 example.id,
//                                 "output"
//                               )}
//                             />
//                           </Col>
//                         </Form.Group>
//                         <Form.Group as={Row}>
//                           <Col sm={{ span: 10, offset: 2 }}>
//                             <Button
//                               type="button"
//                               size="sm"
//                               variant="danger"
//                               onClick={this.handleExampleDelete(example.id)}
//                             >
//                               Delete example
//                             </Button>
//                           </Col>
//                         </Form.Group>
//                       </span>
//                     ))}
//                     <Form.Group as={Row}>
//                       <Col sm={{ span: 10 }}>
//                         <Button
//                           type="button"
//                           variant="primary"
//                           onClick={this.handleExampleAdd}
//                         >
//                           Add example
//                         </Button>
//                       </Col>
//                     </Form.Group>
//                   </div>
//                 )}
//                 <Form.Label>{this.state.description}</Form.Label>
//                 <Form.Control
//                   type="text"
//                   as="textarea"
//                   placeholder="Enter text"
//                   value={this.state.input}
//                   onChange={this.handleInputChange}
//                 />
//               </Form.Group>

//               <Button variant="primary" type="submit">
//                 {this.state.buttonText}
//               </Button>
//             </Form>
//             <div
//               style={{
//                 textAlign: "center",
//                 margin: "20px",
//                 fontSize: "18pt"
//               }}
//             >
//               {this.state.output}
//             </div>
//           </div>
//         </body>
//       </div>
//     );
//   }
// }

// export default App;
