import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import { ModelForm } from './ModelForm'
import { Models } from './Models'
import React from 'react';

const App = () => {
    return <Router>
        <Switch>
            <Route path={'/models/:modelId'} >
                <ModelForm />
            </Route>
            <Route path={'/'} >
                <Models />
            </Route>
        </Switch>
    </Router>
}

export default App;