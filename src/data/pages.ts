import records from './content.json';
export function getDemoPages(){
  const extra=[
    {route:'/donate/',title:'Make a difference',kind:'donate'},
    {route:'/join-us/',title:'There’s a place for you here',kind:'join'},
    {route:'/get-support/',title:'You don’t have to face this alone',kind:'support'},
    {route:'/our-story/',title:'In Paul’s memory',kind:'story'},
    {route:'/resources/',title:'Useful information',kind:'resources'},
  ];
  return [...records.filter(page=>page.route!='/'),...extra.map(page=>({...page,url:'',body:'',paragraphs:[],links:[],images:[],when:'',status:'',sourceBodySha256:''}))];
}
