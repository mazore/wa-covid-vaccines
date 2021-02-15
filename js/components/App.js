const Grid = MaterialUI.Grid;
const Typography = MaterialUI.Typography;

class App extends React.Component {
    constructor() {
        super();

        this.state = {
            lastUpdated: 'loading...',
        };
    }

    componentDidMount() {
        const setScrapes = async () => {
            const response = await getLastUpdated();
            this.setState({lastUpdated: response.val()});
        }
        setScrapes();
    }

    render() {
        return (
            <div className="main">
                <Grid container justify="center" spacing={3}>
                    <Grid item xs={10} sm={8}>
                        <h1 className="heading">WA Covid Vaccines</h1>

                        <Typography className="lastUpdated" variant="h6" display="block">
                            Last updated: {this.state.lastUpdated}
                        </Typography>

                        <Appointments/>

                        <Typography className="footer" variant="caption" display="block" gutterBottom>
                            Github <a href="http://github.com/mazore/wa-covid-vaccines">here</a>
                            <br />
                            Copyright &#169; {new Date().getFullYear()} Evan Mazor. All rights reserved.
                        </Typography>

                        <div style={{ height: 100 }}/>
                    </Grid>
                </Grid>
            </div>
        )
    }
}
