const Button = MaterialUI.Button;

function SignUpLink({ scrape }) {
    return (
        <Button
            className="btn"
            variant="contained"
            color="primary"
            href={scrape.url}
            rel="noreferrer"
            target="_blank"
        >
            {scrape.available ? "Sign Up" : "Website"}
        </Button>
    );
}
