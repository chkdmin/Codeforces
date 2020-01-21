$(document).ready(() => {
    $('.contest-date').each((idx, element) => {
        let started = moment($(element).text());
        let $target = $(element).parent().parent().find('.before-date');

        setInterval(() => {
            $target.text(moment.duration(started.diff(moment())).format("d [days] hh:mm:ss.SSS"));
        });
    });
});
