class Appointments extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            scrapes: []
        };
    }

    componentDidMount() {
        const setScrapes = async () => {
            const response = await getScrapes();
            const obj = response.val();
            this.setState({scrapes: Object.values(obj)});
        }
        setScrapes();
    }

    render() {
        console.log(this.state.scrapes);
        return (
            <div>
                {this.state.scrapes.map((scrape) => (
                    <Card key={scrape.name} scrape={scrape}/>
                ))}
            </div>
        );
    }
};
