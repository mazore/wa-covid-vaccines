const Card = MaterialUI.Card;
const CardContent = MaterialUI.CardContent;
const CardHeader = MaterialUI.CardHeader;

class Appointments extends React.Component {
    constructor() {
        super();

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
        return (
            <div>
                {this.state.scrapes.map((scrape) => (
                    <div key={scrape.name} className="cardBox">
                        <Card elevation={0} className={scrape.available ? "card" : "card card-no-availability"}>
                            <CardHeader
                                className="card-header"
                                title={<div>{scrape.name}</div>}
                                subheader={<div>Address</div>}
                            />
                            <CardContent>
                                <Availability scrape={scrape} />
                                <MoreInformation scrape={scrape} />
                                <SignUpLink scrape={scrape} />
                            </CardContent>
                        </Card>
                    </div>
                ))}
            </div>
        );
    }
};
