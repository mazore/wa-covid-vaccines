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
            const scrapes = Object.values(response.val());
            const available = [];
            const notAvailable = [];
            for (const scrape of scrapes) {
                if (scrape.available) {
                    available.push(scrape);
                } else {
                    notAvailable.push(scrape);
                }
            }
            this.setState({scrapes: available.concat(notAvailable)});
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
                                subheader={<div>{`${scrape.address} ${scrape.zip}`}</div>}
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
